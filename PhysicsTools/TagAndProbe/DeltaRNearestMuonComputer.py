import FWCore.ParameterSet.Config as cms

def DeltaRNearestMuonComputer(**kwargs):
  mod = cms.EDProducer('DeltaRNearestMuonComputer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
