import FWCore.ParameterSet.Config as cms

def PhotonConversionTrajectorySeedProducerFromSingleLeg(**kwargs):
  mod = cms.EDProducer('PhotonConversionTrajectorySeedProducerFromSingleLeg',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
