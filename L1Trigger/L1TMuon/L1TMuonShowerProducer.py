import FWCore.ParameterSet.Config as cms

def L1TMuonShowerProducer(**kwargs):
  mod = cms.EDProducer('L1TMuonShowerProducer',
    showerInput = cms.InputTag('simEmtfShowers', 'EMTF'),
    bxMin = cms.int32(0),
    bxMax = cms.int32(0),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
