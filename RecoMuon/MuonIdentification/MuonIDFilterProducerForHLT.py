import FWCore.ParameterSet.Config as cms

def MuonIDFilterProducerForHLT(**kwargs):
  mod = cms.EDProducer('MuonIDFilterProducerForHLT',
    inputMuonCollection = cms.InputTag('hltIterL3MuonsNoID'),
    applyTriggerIdLoose = cms.bool(True),
    typeMuon = cms.uint32(0),
    allowedTypeMask = cms.uint32(0),
    requiredTypeMask = cms.uint32(0),
    minNMuonHits = cms.int32(0),
    minNMuonStations = cms.int32(0),
    minNTrkLayers = cms.int32(0),
    minTrkHits = cms.int32(0),
    minPixLayer = cms.int32(0),
    minPixHits = cms.int32(0),
    minPt = cms.double(0),
    maxNormalizedChi2 = cms.double(9999),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
