import FWCore.ParameterSet.Config as cms

def MuonAlignmentAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('MuonAlignmentAnalyzer',
    StandAloneTrackCollectionTag = cms.InputTag('globalMuons'),
    GlobalMuonTrackCollectionTag = cms.InputTag('standAloneMuons', 'UpdatedAtVtx'),
    RecHits4DDTCollectionTag = cms.InputTag('dt4DSegments'),
    RecHits4DCSCCollectionTag = cms.InputTag('cscSegments'),
    DataType = cms.untracked.string('RealData'),
    ptRangeMin = cms.untracked.double(0),
    ptRangeMax = cms.untracked.double(300),
    invMassRangeMin = cms.untracked.double(0),
    invMassRangeMax = cms.untracked.double(200),
    doSAplots = cms.untracked.bool(True),
    doGBplots = cms.untracked.bool(True),
    doResplots = cms.untracked.bool(True),
    resLocalXRangeStation1 = cms.untracked.double(0.1),
    resLocalXRangeStation2 = cms.untracked.double(0.3),
    resLocalXRangeStation3 = cms.untracked.double(3),
    resLocalXRangeStation4 = cms.untracked.double(3),
    resLocalYRangeStation1 = cms.untracked.double(0.7),
    resLocalYRangeStation2 = cms.untracked.double(0.7),
    resLocalYRangeStation3 = cms.untracked.double(5),
    resLocalYRangeStation4 = cms.untracked.double(5),
    resThetaRange = cms.untracked.double(0.1),
    resPhiRange = cms.untracked.double(0.1),
    nbins = cms.untracked.int32(500),
    min1DTrackRecHitSize = cms.untracked.int32(1),
    min4DTrackSegmentSize = cms.untracked.int32(1),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
