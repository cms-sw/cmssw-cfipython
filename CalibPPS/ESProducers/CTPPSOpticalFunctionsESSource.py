import FWCore.ParameterSet.Config as cms

def CTPPSOpticalFunctionsESSource(*args, **kwargs):
  mod = cms.ESSource('CTPPSOpticalFunctionsESSource',
    label = cms.string(''),
    configuration = cms.VPSet(
      template = cms.PSetTemplate(
        validityRange = cms.EventRange('0:18446744073709551615-0:18446744073709551615'),
        opticalFunctions = cms.VPSet(
          template = cms.PSetTemplate(
            xangle = cms.required.double,
            fileName = cms.required.FileInPath
          )
        ),
        scoringPlanes = cms.VPSet(
          template = cms.PSetTemplate(
            rpId = cms.required.uint32,
            dirName = cms.required.string,
            z = cms.required.double
          )
        )
      )
    ),
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
