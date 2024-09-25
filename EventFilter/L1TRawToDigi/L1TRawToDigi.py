import FWCore.ParameterSet.Config as cms

def L1TRawToDigi(*args, **kwargs):
  mod = cms.EDProducer('L1TRawToDigi',
    FedIds = cms.vint32(),
    Setup = cms.string(''),
    FWId = cms.uint32(0),
    DmxFWId = cms.uint32(0),
    FWOverride = cms.bool(False),
    TMTCheck = cms.bool(True),
    CTP7 = cms.untracked.bool(False),
    MTF7 = cms.untracked.bool(False),
    InputLabel = cms.InputTag('rawDataCollector'),
    lenSlinkHeader = cms.untracked.int32(8),
    lenSlinkTrailer = cms.untracked.int32(8),
    lenAMCHeader = cms.untracked.int32(8),
    lenAMCTrailer = cms.untracked.int32(0),
    lenAMC13Header = cms.untracked.int32(8),
    lenAMC13Trailer = cms.untracked.int32(8),
    debug = cms.untracked.bool(False),
    MinFeds = cms.uint32(0),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
