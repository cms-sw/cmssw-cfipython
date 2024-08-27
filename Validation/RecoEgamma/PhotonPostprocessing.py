import FWCore.ParameterSet.Config as cms

def PhotonPostprocessing(**kwargs):
  mod = cms.EDAnalyzer('PhotonPostprocessing',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
