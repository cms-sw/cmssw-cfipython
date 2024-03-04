import FWCore.ParameterSet.Config as cms

def ExtractXMLFile(**kwargs):
  mod = cms.EDAnalyzer('ExtractXMLFile',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
