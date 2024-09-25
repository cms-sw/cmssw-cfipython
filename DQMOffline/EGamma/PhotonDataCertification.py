import FWCore.ParameterSet.Config as cms

def PhotonDataCertification(*args, **kwargs):
  mod = cms.EDProducer('PhotonDataCertification',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
