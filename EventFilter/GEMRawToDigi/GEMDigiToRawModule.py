import FWCore.ParameterSet.Config as cms

def GEMDigiToRawModule(**kwargs):
  mod = cms.EDProducer('GEMDigiToRawModule',
    gemDigi = cms.InputTag('simMuonGEMDigis'),
    eventType = cms.int32(0),
    minBunch = cms.int32(-3),
    maxBunch = cms.int32(4),
    useDBEMap = cms.bool(False),
    simulatePulseStretching = cms.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
