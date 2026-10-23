import FWCore.ParameterSet.Config as cms

def CaloTPTableProducer(*args, **kwargs):
  mod = cms.EDProducer('CaloTPTableProducer',
    name = cms.string('l1calotowerflattableproducer'),
    ecalLSB = cms.untracked.double(0.5),
    ecalTPsSrc = cms.InputTag('ecalDigis', 'EcalTriggerPrimitives'),
    ecalTPsName = cms.string('EcalUnpackedTPs'),
    hcalTPsSrc = cms.InputTag('hcalDigis'),
    hcalTPsName = cms.string('HcalUnpackedTPs'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
