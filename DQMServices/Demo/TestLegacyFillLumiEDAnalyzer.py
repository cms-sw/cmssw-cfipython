import FWCore.ParameterSet.Config as cms

def TestLegacyFillLumiEDAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('TestLegacyFillLumiEDAnalyzer',
    folder = cms.string('Legacy/testlegacyfilllumi'),
    howmany = cms.int32(1),
    value = cms.double(1),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
