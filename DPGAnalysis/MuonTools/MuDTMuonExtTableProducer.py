import FWCore.ParameterSet.Config as cms

def MuDTMuonExtTableProducer(*args, **kwargs):
  mod = cms.EDProducer('MuDTMuonExtTableProducer',
    name = cms.string('muon'),
    src = cms.InputTag('patMuons'),
    dtSegmentSrc = cms.InputTag('dt4DSegments'),
    trigEventSrc = cms.InputTag('hltTriggerSummaryAOD', '', 'HLT'),
    trigResultsSrc = cms.InputTag('TriggerResults', '', 'HLT'),
    fillMatches = cms.bool(True),
    trigName = cms.string('HLT_Mu55*'),
    isoTrigName = cms.string('HLT_IsoMu2*'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
