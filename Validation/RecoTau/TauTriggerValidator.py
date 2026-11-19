import FWCore.ParameterSet.Config as cms

def TauTriggerValidator(*args, **kwargs):
  mod = cms.EDProducer('TauTriggerValidator',
    triggerResults = cms.InputTag('TriggerResults', '', 'HLT'),
    trigEvent = cms.InputTag('hltTriggerSummaryAOD', '', 'HLT'),
    hltProcessName = cms.string('HLT'),
    hltPath = cms.required.string,
    label = cms.required.string,
    outFolder = cms.string('HLT/Tau/CrossTriggerValidation'),
    l1SeedModule = cms.string(''),
    ptMax = cms.double(300),
    legs = cms.VPSet(
      template = cms.PSetTemplate(
        objType = cms.required.string,
        multiplicity = cms.uint32(1),
        ptMin = cms.double(20),
        etaMax = cms.double(2.4),
        plateauEtaCut = cms.double(999),
        plateauPtCut = cms.double(0),
        filterName = cms.string(''),
        dR2limit = cms.double(0.1),
        genCollection = cms.InputTag('tauGenJetsSelectorAllHadrons'),
        genParticleCollection = cms.InputTag('genParticles'),
        fromTauDecay = cms.bool(True)
      )
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
