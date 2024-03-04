import FWCore.ParameterSet.Config as cms

def GsfGEDElectronAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('GsfGEDElectronAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
