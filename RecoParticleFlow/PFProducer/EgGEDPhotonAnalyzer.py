import FWCore.ParameterSet.Config as cms

def EgGEDPhotonAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('EgGEDPhotonAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
