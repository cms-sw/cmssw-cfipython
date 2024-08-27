import FWCore.ParameterSet.Config as cms

def TestLegacyEDAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('TestLegacyEDAnalyzer',
    folder = cms.string('Legacy/testlegacy'),
    howmany = cms.int32(1),
    value = cms.double(1),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
