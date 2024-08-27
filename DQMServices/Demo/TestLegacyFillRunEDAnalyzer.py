import FWCore.ParameterSet.Config as cms

def TestLegacyFillRunEDAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('TestLegacyFillRunEDAnalyzer',
    folder = cms.string('Legacy/testlegacyfillrun'),
    howmany = cms.int32(1),
    value = cms.double(1),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
