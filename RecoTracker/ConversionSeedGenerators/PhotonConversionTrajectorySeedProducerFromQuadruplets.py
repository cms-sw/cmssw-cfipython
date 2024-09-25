import FWCore.ParameterSet.Config as cms

def PhotonConversionTrajectorySeedProducerFromQuadruplets(*args, **kwargs):
  mod = cms.EDProducer('PhotonConversionTrajectorySeedProducerFromQuadruplets',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
