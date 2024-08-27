import FWCore.ParameterSet.Config as cms

def TkAlV0sAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('TkAlV0sAnalyzer',
    vertexCompositeCandidates = cms.InputTag('generalV0Candidates', 'Kshort'),
    tracks = cms.InputTag('ALCARECOTkAlKShortTracks'),
    beamSpot = cms.InputTag('offlineBeamSpot'),
    primaryVertex = cms.InputTag('offlinePrimaryVertices'),
    lumiScalers = cms.InputTag('scalersRawToDigi'),
    metadata = cms.InputTag('onlineMetaDataDigis'),
    forceSCAL = cms.bool(False),
    pvNDOF = cms.int32(4),
    histoPSet = cms.PSet(
      lumiPSet = cms.PSet(
        nbins = cms.int32(3700),
        xmin = cms.double(0),
        xmax = cms.double(14000)
      ),
      massPSet = cms.PSet(
        nbins = cms.int32(100),
        xmin = cms.double(0.4),
        xmax = cms.double(0.6)
      ),
      ptPSet = cms.PSet(
        nbins = cms.int32(100),
        xmin = cms.double(0),
        xmax = cms.double(50)
      ),
      etaPSet = cms.PSet(
        nbins = cms.int32(60),
        xmin = cms.double(-3),
        xmax = cms.double(3)
      ),
      LxyPSet = cms.PSet(
        nbins = cms.int32(350),
        xmin = cms.double(0),
        xmax = cms.double(70)
      ),
      chi2oNDFPSet = cms.PSet(
        nbins = cms.int32(100),
        xmin = cms.double(0),
        xmax = cms.double(30)
      ),
      puPSet = cms.PSet(
        nbins = cms.int32(100),
        xmin = cms.double(-0.5),
        xmax = cms.double(99.5)
      ),
      lsPSet = cms.PSet(
        nbins = cms.int32(2000),
        xmin = cms.double(0),
        xmax = cms.double(2000)
      )
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
