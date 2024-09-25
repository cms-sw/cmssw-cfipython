import FWCore.ParameterSet.Config as cms

def ExtractXMLFile(*args, **kwargs):
  mod = cms.EDAnalyzer('ExtractXMLFile',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
