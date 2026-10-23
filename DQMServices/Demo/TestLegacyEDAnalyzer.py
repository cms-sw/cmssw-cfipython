import FWCore.ParameterSet.Config as cms

def TestLegacyEDAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('TestLegacyEDAnalyzer',
    folder = cms.string('Legacy/testlegacy'),
    howmany = cms.int32(1),
    value = cms.double(1),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
