import FWCore.ParameterSet.Config as cms

def BtlSimHitsHarvester(**kwargs):
  mod = cms.EDProducer('BtlSimHitsHarvester',
    folder = cms.string('MTD/BTL/SimHits/'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
