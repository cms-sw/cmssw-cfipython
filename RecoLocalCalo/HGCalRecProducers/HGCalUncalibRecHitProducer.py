import FWCore.ParameterSet.Config as cms

def HGCalUncalibRecHitProducer(**kwargs):
  mod = cms.EDProducer('HGCalUncalibRecHitProducer',
    HGCEEdigiCollection = cms.InputTag('hgcalDigis', 'EE'),
    HGCEEhitCollection = cms.string('HGCEEUncalibRecHits'),
    HGCHEFdigiCollection = cms.InputTag('hgcalDigis', 'HEfront'),
    HGCHEFhitCollection = cms.string('HGCHEFUncalibRecHits'),
    HGCHEBdigiCollection = cms.InputTag('hgcalDigis', 'HEback'),
    HGCHEBhitCollection = cms.string('HGCHEBUncalibRecHits'),
    HGCHFNosedigiCollection = cms.InputTag('hfnoseDigis', 'HFNose'),
    HGCHFNosehitCollection = cms.string('HGCHFNoseUncalibRecHits'),
    HGCEEConfig = cms.PSet(
      isSiFE = cms.bool(True),
      adcNbits = cms.uint32(10),
      adcSaturation = cms.double(100),
      tdcNbits = cms.uint32(12),
      tdcSaturation = cms.double(10000),
      tdcOnset = cms.double(60),
      toaLSB_ns = cms.double(0.0244),
      tofDelay = cms.double(-9),
      fCPerMIP = cms.vdouble(
        1.25,
        2.57,
        3.88
      )
    ),
    HGCHEFConfig = cms.PSet(
      isSiFE = cms.bool(True),
      adcNbits = cms.uint32(10),
      adcSaturation = cms.double(100),
      tdcNbits = cms.uint32(12),
      tdcSaturation = cms.double(10000),
      tdcOnset = cms.double(60),
      toaLSB_ns = cms.double(0.0244),
      tofDelay = cms.double(-11),
      fCPerMIP = cms.vdouble(
        1.25,
        2.57,
        3.88
      )
    ),
    HGCHEBConfig = cms.PSet(
      isSiFE = cms.bool(True),
      adcNbits = cms.uint32(10),
      adcSaturation = cms.double(68.75),
      tdcNbits = cms.uint32(12),
      tdcSaturation = cms.double(1000),
      tdcOnset = cms.double(55),
      toaLSB_ns = cms.double(0.0244),
      tofDelay = cms.double(-14),
      fCPerMIP = cms.vdouble(
        1,
        1,
        1
      )
    ),
    HGCHFNoseConfig = cms.PSet(
      isSiFE = cms.bool(False),
      adcNbits = cms.uint32(10),
      adcSaturation = cms.double(100),
      tdcNbits = cms.uint32(12),
      tdcSaturation = cms.double(10000),
      tdcOnset = cms.double(60),
      toaLSB_ns = cms.double(0.0244),
      tofDelay = cms.double(-33),
      fCPerMIP = cms.vdouble(
        1.25,
        2.57,
        3.88
      )
    ),
    algo = cms.string('HGCalUncalibRecHitWorkerWeights'),
    computeLocalTime = cms.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
