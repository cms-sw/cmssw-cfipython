import FWCore.ParameterSet.Config as cms

def SmearedCaloJetProducer(*args, **kwargs):
  mod = cms.EDProducer('SmearedCaloJetProducer',
    src = cms.required.InputTag,
    enabled = cms.required.bool,
    rho = cms.required.InputTag,
    variation = cms.int32(0),
    uncertaintySource = cms.string(''),
    seed = cms.uint32(37428479),
    skipGenMatching = cms.bool(False),
    useDeterministicSeed = cms.bool(True),
    debug = cms.untracked.bool(False),
    algo = cms.required.string,
    algopt = cms.required.string,
    genJets = cms.required.InputTag,
    dRMax = cms.required.double,
    dPtMaxFactor = cms.required.double,
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
