import FWCore.ParameterSet.Config as cms

def GEMDigiToRawModule(*args, **kwargs):
  mod = cms.EDProducer('GEMDigiToRawModule',
    gemDigi = cms.InputTag('simMuonGEMDigis'),
    eventType = cms.int32(0),
    minBunch = cms.int32(-3),
    maxBunch = cms.int32(4),
    useDBEMap = cms.bool(False),
    simulatePulseStretching = cms.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
