import FWCore.ParameterSet.Config as cms

def L1PhotonRecoTreeProducer(**kwargs):
  mod = cms.EDAnalyzer('L1PhotonRecoTreeProducer',
    maxPhoton = cms.uint32(20),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
