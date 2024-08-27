import FWCore.ParameterSet.Config as cms

def TestLegacyHarvester(**kwargs):
  mod = cms.EDAnalyzer('TestLegacyHarvester',
    folder = cms.string('LegacyHarvester/'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
