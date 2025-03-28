import FWCore.ParameterSet.Config as cms

def L1TauTriggerFilterObjectProducer(*args, **kwargs):
  mod = cms.EDFilter('L1TauTriggerFilterObjectProducer',
    saveTags = cms.bool(True),
    taus = cms.InputTag('hltGtStage2Digis', 'Tau'),
    selectedBx = cms.vint32(),
    minPt = cms.double(0),
    minHwIso = cms.int32(0),
    nExpected = cms.int32(0),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
