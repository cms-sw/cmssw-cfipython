import FWCore.ParameterSet.Config as cms

def PhotonConversionTrajectorySeedProducerFromQuadruplets(**kwargs):
  mod = cms.EDProducer('PhotonConversionTrajectorySeedProducerFromQuadruplets',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
