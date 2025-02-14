import FWCore.ParameterSet.Config as cms

def RunLumiESAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('RunLumiESAnalyzer',
    esInputTag = cms.ESInputTag('', ''),
    checkDataProductContents = cms.bool(True),
    getIntProduct = cms.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
