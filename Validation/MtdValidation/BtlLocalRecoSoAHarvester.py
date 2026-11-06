import FWCore.ParameterSet.Config as cms

def BtlLocalRecoSoAHarvester(*args, **kwargs):
  mod = cms.EDProducer('BtlLocalRecoSoAHarvester',
    folder = cms.string('MTD/BTL/LocalRecoSoA/'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
