import FWCore.ParameterSet.Config as cms

def DeltaRNearestMuonComputer(*args, **kwargs):
  mod = cms.EDProducer('DeltaRNearestMuonComputer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
