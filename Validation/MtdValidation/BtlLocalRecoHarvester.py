import FWCore.ParameterSet.Config as cms

def BtlLocalRecoHarvester(**kwargs):
  mod = cms.EDProducer('BtlLocalRecoHarvester',
    folder = cms.string('MTD/BTL/LocalReco/'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
