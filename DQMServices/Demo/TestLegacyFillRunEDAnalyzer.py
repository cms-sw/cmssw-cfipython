import FWCore.ParameterSet.Config as cms

def TestLegacyFillRunEDAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('TestLegacyFillRunEDAnalyzer',
    folder = cms.string('Legacy/testlegacyfillrun'),
    howmany = cms.int32(1),
    value = cms.double(1),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
