import FWCore.ParameterSet.Config as cms

def BTLDigiSoAProducer(*args, **kwargs):
  mod = cms.EDProducer('BTLDigiSoAProducer',
    btlDigiCollection = cms.InputTag('mix', 'MTDBarrel'),
    digiCollectionSoATag = cms.string('MTDBarrelSoA'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
