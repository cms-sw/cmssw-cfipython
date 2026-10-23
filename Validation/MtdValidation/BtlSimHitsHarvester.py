import FWCore.ParameterSet.Config as cms

def BtlSimHitsHarvester(*args, **kwargs):
  mod = cms.EDProducer('BtlSimHitsHarvester',
    folder = cms.string('MTD/BTL/SimHits/'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
