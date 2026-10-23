import FWCore.ParameterSet.Config as cms

def L1PhotonRecoTreeProducer(*args, **kwargs):
  mod = cms.EDAnalyzer('L1PhotonRecoTreeProducer',
    maxPhoton = cms.uint32(20),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
