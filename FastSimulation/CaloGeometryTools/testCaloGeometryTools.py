import FWCore.ParameterSet.Config as cms

def testCaloGeometryTools(**kwargs):
  mod = cms.EDAnalyzer('testCaloGeometryTools',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
