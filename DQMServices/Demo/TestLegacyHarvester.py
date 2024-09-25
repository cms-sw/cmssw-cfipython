import FWCore.ParameterSet.Config as cms

def TestLegacyHarvester(*args, **kwargs):
  mod = cms.EDAnalyzer('TestLegacyHarvester',
    folder = cms.string('LegacyHarvester/'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
