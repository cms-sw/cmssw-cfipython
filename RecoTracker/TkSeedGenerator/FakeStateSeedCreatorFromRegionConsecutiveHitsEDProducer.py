import FWCore.ParameterSet.Config as cms

def FakeStateSeedCreatorFromRegionConsecutiveHitsEDProducer(*args, **kwargs):
  mod = cms.EDProducer('FakeStateSeedCreatorFromRegionConsecutiveHitsEDProducer',
    seedingHitSets = cms.InputTag('hitPairEDProducer'),
    SeedComparitorPSet = cms.PSet(
      ComponentName = cms.string('none')
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
