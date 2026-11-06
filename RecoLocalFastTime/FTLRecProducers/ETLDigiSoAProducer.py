import FWCore.ParameterSet.Config as cms

def ETLDigiSoAProducer(*args, **kwargs):
  mod = cms.EDProducer('ETLDigiSoAProducer',
    etlDigiCollection = cms.InputTag('mix', 'MTDEndcap'),
    digiCollectionSoATag = cms.string('MTDEndcapSoA'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
