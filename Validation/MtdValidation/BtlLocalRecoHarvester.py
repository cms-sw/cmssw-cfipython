import FWCore.ParameterSet.Config as cms

def BtlLocalRecoHarvester(*args, **kwargs):
  mod = cms.EDProducer('BtlLocalRecoHarvester',
    folder = cms.string('MTD/BTL/LocalReco/'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
