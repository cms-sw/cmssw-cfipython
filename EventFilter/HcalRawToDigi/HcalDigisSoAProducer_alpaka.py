import FWCore.ParameterSet.Config as cms

def HcalDigisSoAProducer_alpaka(**kwargs):
  mod = cms.EDProducer('HcalDigisSoAProducer@alpaka',
    hbheDigisLabel = cms.InputTag('hcalDigis'),
    qie11DigiLabel = cms.InputTag('hcalDigis'),
    digisLabelF01HE = cms.string('f01HEDigis'),
    digisLabelF5HB = cms.string('f5HBDigis'),
    digisLabelF3HB = cms.string('f3HBDigis'),
    maxChannelsF01HE = cms.uint32(10000),
    maxChannelsF5HB = cms.uint32(10000),
    maxChannelsF3HB = cms.uint32(10000),
    mightGet = cms.optional.untracked.vstring,
    alpaka = cms.untracked.PSet(
      backend = cms.untracked.string('')
    )
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
