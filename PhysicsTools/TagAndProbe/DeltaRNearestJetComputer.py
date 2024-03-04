import FWCore.ParameterSet.Config as cms

def DeltaRNearestJetComputer(**kwargs):
  mod = cms.EDProducer('DeltaRNearestJetComputer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
