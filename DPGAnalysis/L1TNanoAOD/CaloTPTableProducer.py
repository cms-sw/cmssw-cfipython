import FWCore.ParameterSet.Config as cms

def CaloTPTableProducer(**kwargs):
  mod = cms.EDProducer('CaloTPTableProducer',
    name = cms.string('l1calotowerflattableproducer'),
    ecalLSB = cms.untracked.double(0.5),
    ecalTPsSrc = cms.InputTag('ecalDigis', 'EcalTriggerPrimitives'),
    ecalTPsName = cms.string('EcalUnpackedTPs'),
    hcalTPsSrc = cms.InputTag('hcalDigis'),
    hcalTPsName = cms.string('HcalUnpackedTPs'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
