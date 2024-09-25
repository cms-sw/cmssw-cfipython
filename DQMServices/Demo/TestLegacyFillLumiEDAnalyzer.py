import FWCore.ParameterSet.Config as cms

def TestLegacyFillLumiEDAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('TestLegacyFillLumiEDAnalyzer',
    folder = cms.string('Legacy/testlegacyfilllumi'),
    howmany = cms.int32(1),
    value = cms.double(1),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
