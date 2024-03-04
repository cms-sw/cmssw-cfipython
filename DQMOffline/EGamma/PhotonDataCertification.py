import FWCore.ParameterSet.Config as cms

def PhotonDataCertification(**kwargs):
  mod = cms.EDProducer('PhotonDataCertification',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
