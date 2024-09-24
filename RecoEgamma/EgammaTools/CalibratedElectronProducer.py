import FWCore.ParameterSet.Config as cms

def CalibratedElectronProducer(*args, **kwargs):
  mod = cms.EDProducer('CalibratedElectronProducer',
    src = cms.InputTag('gedPhotons'),
    epCombConfig = cms.PSet(
      ecalTrkRegressionConfig = cms.PSet(
        rangeMinLowEt = cms.double(-1),
        rangeMaxLowEt = cms.double(3),
        rangeMinHighEt = cms.double(-1),
        rangeMaxHighEt = cms.double(3),
        lowEtHighEtBoundary = cms.double(50),
        forceHighEnergyTrainingIfSaturated = cms.bool(False),
        ebLowEtForestName = cms.ESInputTag('', 'electron_eb_ECALTRK_lowpt'),
        ebHighEtForestName = cms.ESInputTag('', 'electron_eb_ECALTRK'),
        eeLowEtForestName = cms.ESInputTag('', 'electron_ee_ECALTRK_lowpt'),
        eeHighEtForestName = cms.ESInputTag('', 'electron_ee_ECALTRK')
      ),
      ecalTrkRegressionUncertConfig = cms.PSet(
        rangeMinLowEt = cms.double(-1),
        rangeMaxLowEt = cms.double(3),
        rangeMinHighEt = cms.double(-1),
        rangeMaxHighEt = cms.double(3),
        lowEtHighEtBoundary = cms.double(50),
        forceHighEnergyTrainingIfSaturated = cms.bool(False),
        ebLowEtForestName = cms.ESInputTag('', 'electron_eb_ECALTRK_lowpt'),
        ebHighEtForestName = cms.ESInputTag('', 'electron_eb_ECALTRK'),
        eeLowEtForestName = cms.ESInputTag('', 'electron_ee_ECALTRK_lowpt'),
        eeHighEtForestName = cms.ESInputTag('', 'electron_ee_ECALTRK')
      ),
      maxEcalEnergyForComb = cms.double(200),
      minEOverPForComb = cms.double(0.025),
      maxEPDiffInSigmaForComb = cms.double(15),
      maxRelTrkMomErrForComb = cms.double(10)
    ),
    recHitCollectionEB = cms.InputTag('reducedEcalRecHitsEB'),
    recHitCollectionEE = cms.InputTag('reducedEcalRecHitsEE'),
    correctionFile = cms.string(''),
    minEtToCalibrate = cms.double(5),
    produceCalibratedObjs = cms.bool(True),
    semiDeterministic = cms.bool(True),
    valueMapsStored = cms.vstring(
      'energyScaleStatUp',
      'energyScaleStatDown',
      'energyScaleSystUp',
      'energyScaleSystDown',
      'energyScaleGainUp',
      'energyScaleGainDown',
      'energySigmaRhoUp',
      'energySigmaRhoDown',
      'energySigmaPhiUp',
      'energySigmaPhiDown',
      'energyScaleUp',
      'energyScaleDown',
      'energySigmaUp',
      'energySigmaDown',
      'energyScaleValue',
      'energySigmaValue',
      'energySmearNrSigma',
      'ecalEnergyPreCorr',
      'ecalEnergyErrPreCorr',
      'ecalEnergyPostCorr',
      'ecalEnergyErrPostCorr',
      'ecalTrkEnergyPreCorr',
      'ecalTrkEnergyErrPreCorr',
      'ecalTrkEnergyPostCorr',
      'ecalTrkEnergyErrPostCorr'
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod