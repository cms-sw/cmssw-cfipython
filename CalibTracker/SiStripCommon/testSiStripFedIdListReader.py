import FWCore.ParameterSet.Config as cms

def testSiStripFedIdListReader(**kwargs):
  mod = cms.EDAnalyzer('testSiStripFedIdListReader',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
