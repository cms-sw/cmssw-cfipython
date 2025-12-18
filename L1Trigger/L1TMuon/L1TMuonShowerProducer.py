import FWCore.ParameterSet.Config as cms

def L1TMuonShowerProducer(*args, **kwargs):
  mod = cms.EDProducer('L1TMuonShowerProducer',
    showerInput = cms.InputTag('simEmtfShowers', 'EMTF'),
    bxMin = cms.int32(0),
    bxMax = cms.int32(0),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
