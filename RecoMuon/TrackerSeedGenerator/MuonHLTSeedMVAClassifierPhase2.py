import FWCore.ParameterSet.Config as cms

def MuonHLTSeedMVAClassifierPhase2(**kwargs):
  mod = cms.EDProducer('MuonHLTSeedMVAClassifierPhase2',
    src = cms.InputTag('hltIter2Phase2L3FromL1TkMuonPixelSeeds'),
    L1TkMu = cms.InputTag('L1TkMuons', 'Muon'),
    mvaFile_B_0 = cms.FileInPath('RecoMuon/TrackerSeedGenerator/data/xgb_Phase2_Iter2FromL1_barrel_v0.xml'),
    mvaFile_E_0 = cms.FileInPath('RecoMuon/TrackerSeedGenerator/data/xgb_Phase2_Iter2FromL1_endcap_v0.xml'),
    mvaScaleMean_B = cms.vdouble(
      0.00033113700731766336,
      1.6825601468762878e-06,
      1.7909321225248029e-06,
      0.010534608406382916,
      0.0059694599573301386,
      0.00096050222549711134,
      0.043841896727814661,
      7.8467412376082371e-05,
      0.40725050850004824,
      0.41125151617410227,
      0.39815551065544846
    ),
    mvaScaleStd_B = cms.vdouble(
      0.00060429483637986241,
      2.445644111872427e-06,
      3.454992543447134e-06,
      0.094015816288872553,
      0.79788069475737655,
      0.49329330445359282,
      0.04180518265631776,
      0.058296511682094855,
      0.40718570093735768,
      0.41337782307392973,
      0.41011603495495341
    ),
    mvaScaleMean_E = cms.vdouble(
      0.00022658482374555603,
      5.3589219737840455e-07,
      1.010003713549798e-06,
      0.00078868736122246149,
      0.0011977305488424081,
      -0.0030252353426003594,
      0.071519448041712536,
      -0.00069406267751090259,
      0.20535152195939896,
      0.29668165337838243,
      0.28798220230180455
    ),
    mvaScaleStd_E = cms.vdouble(
      0.00038577267890499558,
      1.4853721474087994e-06,
      6.9829970367365643e-06,
      0.040713407576660837,
      0.58976065600953986,
      0.33052121398064654,
      0.055893867865419493,
      0.088062735333885464,
      0.32545869026656121,
      0.32933544962313771,
      0.31798997945780721
    ),
    doSort = cms.bool(True),
    nSeedsMax_B = cms.int32(20),
    nSeedsMax_E = cms.int32(20),
    mvaCut_B = cms.double(0),
    mvaCut_E = cms.double(0),
    etaEdge = cms.double(1.2),
    baseScore = cms.double(0.5),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod