import FWCore.ParameterSet.Config as cms

def EcalSelectiveReadoutProducer(**kwargs):
  mod = cms.EDProducer('EcalSelectiveReadoutProducer',
    digiProducer = cms.required.string,
    EBdigiCollection = cms.required.string,
    EEdigiCollection = cms.required.string,
    EBSRPdigiCollection = cms.required.string,
    EESRPdigiCollection = cms.required.string,
    EBSrFlagCollection = cms.required.string,
    EESrFlagCollection = cms.required.string,
    trigPrimProducer = cms.required.string,
    trigPrimCollection = cms.required.string,
    trigPrimBypass = cms.required.bool,
    trigPrimBypassMode = cms.required.int32,
    dumpFlags = cms.untracked.int32(0),
    writeSrFlags = cms.untracked.bool(False),
    produceDigis = cms.untracked.bool(True),
    configFromCondDB = cms.bool(False),
    UseFullReadout = cms.required.bool,
    defaultTtf = cms.required.int32,
    trigPrimBypassWithPeakFinder = cms.required.bool,
    trigPrimBypassLTH = cms.required.double,
    trigPrimBypassHTH = cms.required.double,
    deltaPhi = cms.optional.int32,
    deltaEta = cms.optional.int32,
    ecalDccZs1stSample = cms.optional.int32,
    ebDccAdcToGeV = cms.optional.double,
    eeDccAdcToGeV = cms.optional.double,
    dccNormalizedWeights = cms.optional.vdouble,
    symetricZS = cms.optional.bool,
    srpBarrelLowInterestChannelZS = cms.optional.double,
    srpEndcapLowInterestChannelZS = cms.optional.double,
    srpBarrelHighInterestChannelZS = cms.optional.double,
    srpEndcapHighInterestChannelZS = cms.optional.double,
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
