import FWCore.ParameterSet.Config as cms

def MTDDigiGeometryAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('MTDDigiGeometryAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
